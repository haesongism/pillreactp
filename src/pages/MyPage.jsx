import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { Link } from 'react-router-dom';

export const MyPage = () => {
  return (
    <MainContainer>
      <span>My Page</span>
    </MainContainer>
  );
};

const MainContainer = styled.div`
  width: 100%;
  height: auto;
  background-color: #d3b9eb;
  position: relative;
  display: flex;
  justify-content: center;
`;
