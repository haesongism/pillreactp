import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { Link, useNavigate } from 'react-router-dom';

function Main() {
  const navigate = useNavigate();

  return (
    <MainContainer>
      <MainHeader>
        <Link to="/">
          <Img
            width={200}
            height={80}
            alt=""
            src="http://localhost:3000/img/logo.jpg"
          />
        </Link>
        <MenuBox>
          <IndividualMenu
            onClick={() => {
              navigate('/mypage');
            }}
          >
            마이페이지
          </IndividualMenu>
          <IndividualMenu
            onClick={() => {
              navigate('/login');
            }}
          >
            로그인
          </IndividualMenu>
          <IndividualMenu>로그아웃</IndividualMenu>
        </MenuBox>
      </MainHeader>
      <ContentBox>
        <ContentImg>
          <span style={{ fontSize: 30, fontWeight: 500, alignSelf: 'center' }}>
            당신의 약을 알아보세요.
          </span>
          <Img
            width={400}
            height={400}
            alt=""
            src="http://localhost:3000/img/drug.png"
          />
        </ContentImg>
        <SearchContainer>
          <Searching />
        </SearchContainer>
      </ContentBox>
    </MainContainer>
  );
}

const Searching = () => {
  const [search, setSearch] = useState('');

  const [result, setResult] = useState([]);
  const onChange = e => {
    setSearch(e.target.value);
  };

  useEffect(() => {
    console.log(search);
  }, [search]);

  const onSearch = value => {
    console.log('검색어는', value);
  };

  return (
    <>
      <Form
        onSubmit={e => {
          e.preventDefault();
          console.log(search);
          onSearch(search);
        }}
      >
        <input
          type="text"
          value={search}
          onChange={onChange}
          placeholder={'검색어를 입력하세요.'}
          style={{
            width: '900px',
            height: '40px',
            borderRadius: '10px',
            borderWidth: 0.5,
            borderColor: '#efefef',
          }}
        />
        <button
          style={{
            color: '#EDEDED',
            width: '100px',
            height: '40px',
            borderRadius: '10px',
            background: '#949BA0',
            borderWidth: 0.5,
            borderColor: '#dcdcdc',
          }}
          type="submit"
        >
          찾기
        </button>
      </Form>
      {/* 검색결과 */}
      <SearchBox>
        <span>검색 결과 나오는 부분</span>
      </SearchBox>
    </>
  );
};

export default Main;

const MainContainer = styled.div`
  width: 100%;
  height: auto;
  background-color: #f5f6f7;
  position: relative;
  display: flex;
  justify-content: center;
`;

const MainHeader = styled.div`
  width: 98%;
  height: 80px;
  position: fixed;
  top: 0;
  /* background-color: red; */
  display: flex;
  justify-content: space-between;
`;

const MenuBox = styled.div`
  width: 25%;
  height: 100%;
  /* background-color: yellow; */
  display: flex;
  justify-content: space-around;
  align-items: center;
`;

const IndividualMenu = styled.span`
  display: block;
  width: 30%;
  height: 50%;
  /* background-color: purple; */
  text-align: center;
  font-size: 20px;
  line-height: 36px;
  cursor: pointer;
`;

const Img = styled.img`
  margin: 4px 12px 0 0;
  cursor: pointer;
`;

const ContentBox = styled.div`
  width: 100%;
  height: 1600px;
  margin-top: 80px;
  /* background-color: pink; */
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const ContentImg = styled.div`
  width: 98%;
  height: 400px;
  background-image: linear-gradient(
      54deg,
      rgba(255, 131, 122, 0.25),
      rgba(255, 131, 122, 0) 28%
    ),
    linear-gradient(
      241deg,
      rgba(239, 152, 207, 0.25),
      rgba(239, 152, 207, 0) 36%
    );
  display: flex;
  justify-content: space-evenly;
`;

const SearchContainer = styled.div`
  width: 90%;
  height: 600px;
  /* background-color: orange; */
`;

const SearchBox = styled.div`
  width: 80%;
  height: 500px;
  background-color: #efefef;
  margin: 0 auto;
`;

const Form = styled.form`
  width: 80%;
  height: 80px;
  /* background: red; */
  margin: 0 auto;
  display: flex;
  justify-content: space-around;
  align-items: center;
`;
