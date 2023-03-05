from django.shortcuts import render
from django.http import HttpResponse
# 일반 스트링이 아닌 http response를 return해야 한다.
from .models import Review
# 모든 Review의 정보를 가져와서 출력하기 위해

# Create your views here.
def see_all_reviews(request):
    # 인자로 request object를 제공해서 정보를 사용할 수 있다.
    try:
        reviews = Review.objects.all()
        # object = 매니저, all = DB에서 모든 정보를 call
        return render(
            request,
            "all_reviews.html",
            {
            "reviews":reviews,
            "title":"게시판 리스트",
            },
            )
    # render(request, "불러올 html파일", dict타입 {"html로 보낼 data이름":data 이름})
    except Review.DoesNotExist:
        return render(
            request,
            "all_reviews.html",
            {
            'not_found':True,
            },
            )

def see_one_reviews(request, review_pk):
    try:   
        review = Review.objects.get(pk=review_pk)
        return render(
                request,
                "review_detail.html",
                {
                "review":review,
                },
                )
    # review.urls 에서 지정한 path의 int타입 파라미터를 review_id로 받아 사용할 수 있다.
    except Review.DoesNotExist:
        return render(
            request,
            "review_detail.html",
            {
            'not_found':True,
            },
            )
