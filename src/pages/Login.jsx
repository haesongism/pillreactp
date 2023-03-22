import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { Link, useNavigate } from 'react-router-dom';

export const Login = () => {
  const [id, setId] = useState('');
  const [pw, setPw] = useState('');

  const onChangeId = e => {
    console.log('ㅇㄷ', e.target.value);
    setId(e.target.value);
  };
  const onChangePw = e => {
    console.log('ㅂㅂ', e.target.value);
    setPw(e.target.value);
  };
  return (
    <MainContainer>
      <Img
        width={200}
        height={200}
        alt=""
        src="http://localhost:3000/img/lock.png"
      />
      <Form
        onSubmit={e => {
          e.preventDefault();
          console.log('제출');
          console.log(id, pw);
        }}
        method="post"
        // action=""
      >
        <ul>
          <li>
            <input
              type="text"
              name="userid"
              placeholder="아이디를 입력해주세요."
              value={id}
              onChange={onChangeId}
            />
          </li>
          <li>
            <input
              type="password"
              name="userpw"
              placeholder="패스워드를 입력해주세요."
              value={pw}
              onChange={onChangePw}
            />
          </li>
          <li>
            <input type="submit" value="로그인" />
          </li>
        </ul>
      </Form>
    </MainContainer>
  );
};

const MainContainer = styled.div`
  width: 100%;
  height: 600px;
  /* background-color: #d3b9eb; */
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
`;

const Form = styled.form`
  width: 50%;
  height: 200px;
  /* background: red; */
  margin: 0 auto;
  display: flex;
  justify-content: space-around;
  align-items: center;
`;
const Img = styled.img`
  margin: 0 auto;
  margin-top: 0px;
`;
