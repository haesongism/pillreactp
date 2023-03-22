import React from 'react';
import styled from 'styled-components';

function Jeon() {
  return (
    <MainBox>
      <MainWrapper>
        <div>
          <p>전혜성 바보!</p>
        </div>
      </MainWrapper>
    </MainBox>
  );
}

const MainBox = styled.div`
  width: 100%;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  background-color: #c8c8c8;
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

  div {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 600px;
  }
`;

export default Jeon;
