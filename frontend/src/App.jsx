import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import PolicyAssistant from './components/PolicyAssistant';
import FindCare from './components/FindCare';
import Checklist from './components/Checklist';
import './styles.css';

function App() {
  return (
    <div className="app">
      <Header />
      <main className="main-content">
        <Hero />
        <PolicyAssistant />
        <FindCare />
        <Checklist />
      </main>
    </div>
  );
}

export default App;
