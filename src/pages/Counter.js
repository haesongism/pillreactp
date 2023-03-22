import React from 'react';
import styled from 'styled-components';
import './counter.css';
function Counter() {
  return (
    <>
      <div id="Announcement-Bar" class="banner-section wf-section">
        <div class="banner-container w-container">
          <div class="banner">
            <div class="banner-text">
              찾으신 일반의약품은 의사 진료없이 바로 구매 가능합니다.
              <a
                href="https://www.nikolaibain.com/templates"
                target="_blank"
                class="banner-link"
              >
                내 주변 약국확인하기
              </a>
            </div>
          </div>
        </div>
      </div>
      <div
        data-collapse="small"
        data-animation="default"
        data-duration="400"
        data-easing="ease"
        data-easing2="ease"
        role="banner"
        class="nav-bar w-nav"
      >
        <div class="nav-container w-container">
          <div class="logo-div">
            <a
              href="index.html"
              aria-current="page"
              class="nav-logo w-inline-block w--current"
            ></a>
          </div>

          <div class="menu-button w-nav-button"></div>
        </div>
      </div>
      <div class="page-wrapper">
        <div class="section light-color-gradient wf-section">
          <div class="container">
            <div class="w-layout-grid hero-grid">
              <div class="text-box _500px">
                <h1 class="heading h1">당신의 약을 알아보세요.</h1>
                <p class="paragraph large">
                  반드시 의사 또는 약사와 의약품 복용에 대한 진료를 받으시고
                  결정하세요.
                </p>
                <div class="spacer _16"></div>
                <a href="contact.html" class="button w-button">
                  의약품 상세검색
                </a>
              </div>
            </div>
          </div>
        </div>
        <div
          data-collapse="small"
          data-animation="default"
          data-duration="400"
          data-easing="ease"
          data-easing2="ease"
          role="banner"
          class="nav-bar w-nav"
        >
          <div class="nav-container w-container">
            <div class="logo-div">
              <a
                href="index.html"
                aria-current="page"
                class="nav-logo w-inline-block w--current"
              ></a>
            </div>

            <div class="menu-button w-nav-button"></div>
          </div>
        </div>
        <div class="page-wrapper">
          <div class="section light-color-gradient wf-section">
            <div class="container">
              <div class="w-layout-grid hero-grid">
                <div class="text-box _500px">
                  <h1 class="heading h1">당신의 약을 알아보세요.</h1>
                  <p class="paragraph large">
                    반드시 의사 또는 약사와 의약품 복용에 대한 진료를 받으시고
                    결정하세요.
                  </p>
                  <div class="spacer _16"></div>
                  <a href="contact.html" class="button w-button">
                    의약품 상세검색
                  </a>
                </div>
              </div>
            </div>
          </div>
          <div
            data-collapse="small"
            data-animation="default"
            data-duration="400"
            data-easing="ease"
            data-easing2="ease"
            role="banner"
            class="nav-bar w-nav"
          >
            <div class="nav-container w-container">
              <div class="logo-div">
                <a
                  href="index.html"
                  aria-current="page"
                  class="nav-logo w-inline-block w--current"
                ></a>
              </div>

              <div class="menu-button w-nav-button"></div>
            </div>
          </div>
          <div class="section wf-section">
            <div class="container">
              <div class="section-top">
                <h2 class="heading h3">의약품 찾기</h2>
                <a
                  href="resources.html"
                  class="button light mobile-hidden w-button"
                >
                  See All Resources
                </a>
              </div>
              <div class="w-dyn-list">
                <div role="list" class="large-3-grid w-dyn-items">
                  <div role="listitem" class="ebook-box w-dyn-item">
                    <a href="#" class="ebook-thumbnail w-inline-block"></a>
                    <div class="paragraph small"></div>
                    <a href="#" class="card-text-link w-inline-block">
                      <h2 class="heading h3"></h2>
                      <p class="paragraph small"></p>
                    </a>
                  </div>
                </div>
                <div class="w-dyn-empty">
                  <div>No items found.</div>
                </div>
              </div>
            </div>
          </div>
          <div class="section black-gradient wf-section">
            <div class="container w-container">
              <div class="text-box _550px center-align">
                <h2 class="heading h2">Get more great resources</h2>
                <p class="paragraph large">
                  Get the latest design resources from across the web. Straight
                  to your inbox.
                </p>
                <div class="spacer _16"></div>
                <div class="email-form center-align w-form">
                  <div class="form-success dark w-form-done">
                    <div>You&#x27;re all signed up.</div>
                  </div>
                  <div class="w-form-fail">
                    <div>검색 결과가 없습니다.</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="footer wf-section">
            <div class="footer-container w-container">
              <div class="w-layout-grid footer-grid">
                <div
                  id="w-node-b8d7be4a-ce45-83ab-5947-02d204c8bff0-cf3fcb86"
                  class="footer-logo-block"
                >
                  <a
                    data-ix="logo"
                    href="index.html"
                    aria-current="page"
                    class="footer-logo w-nav-brand w--current"
                  ></a>
                  <div class="spacer _16"></div>
                  <div class="paragraph small">
                    © 2023 Pill Finder projecct team. All Rights Reserved.
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

const MainBox = styled.div`
  width: 100%;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  background-color: 'pink';
`;

const MainWrapper = styled.div`
  width: 450px;
  height: 600px;
  background-color: white;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  border-radius: 20px;
`;

export default Counter;
