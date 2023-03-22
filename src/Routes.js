import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Main from './pages/Main';
import Gyuri from './pages/Gyuri';
import Jeon from './pages/Jeon';
import Counter from './pages/Counter';
import { MyPage } from './pages/MyPage';
import { Login } from './pages/Login';

function Router() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/gyuri" element={<Gyuri />} />
        <Route path="/jeon" element={<Jeon />} />
        <Route path="/counter" element={<Counter />} />
        <Route path="/mypage" element={<MyPage />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}

export default Router;
