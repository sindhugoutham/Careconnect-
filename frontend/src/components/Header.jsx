import React from 'react';

const Header = () => {
  return (
    <header className="header">
      <h1>CareConnect</h1>
      <nav>
        <button className="nav-btn" style={{ background: 'transparent', color: 'var(--primary-color)', border: '1px solid var(--primary-color)' }}>
          Sign In
        </button>
      </nav>
    </header>
  );
};

export default Header;
