import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';

export const MyPage = () => {
  return (
    <MainContainer>
      <span>마이페이지</span>
    </MainContainer>
  );
};

const MainContainer = styled.div`
  width: 100%;
  height: auto;
  background-color: #2E327A;
  position: relative;
  display: flex;
  justify-content: center;
`;
