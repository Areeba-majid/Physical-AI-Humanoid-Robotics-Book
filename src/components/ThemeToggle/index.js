/** @jsxRuntime classic */
/** @jsx jsx */
import { jsx } from 'theme-ui';
import React, { useEffect, useState } from 'react';

const ThemeToggle = () => {
  const [theme, setTheme] = useState('light');
  const [isMounted, setIsMounted] = useState(false);

  useEffect(() => {
    setIsMounted(true);
    // Check system preference or saved preference
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (savedTheme) {
      setTheme(savedTheme);
    } else if (systemPrefersDark) {
      setTheme('dark');
    }
  }, []);

  useEffect(() => {
    // Apply theme to document
    if (theme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.setAttribute('data-theme', 'light');
      document.documentElement.classList.remove('dark');
    }

    // Save preference
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  // Don't render until mounted to avoid SSR issues
  if (!isMounted) {
    return (
      <button
        aria-label="Loading theme"
        sx={{
          variant: 'styles.button',
          bg: 'muted',
          borderRadius: 'circle',
          p: 2,
          cursor: 'default',
          border: 'none',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          opacity: 0,
          width: '40px',
          height: '40px',
          position: 'relative',
          overflow: 'hidden'
        }}
      >
        <span role="img" aria-label="loading">
          ⏳
        </span>
      </button>
    );
  }

  return (
    <button
      onClick={toggleTheme}
      aria-label={`Switch to ${theme === 'light' ? 'dark' : 'light'} mode`}
      sx={{
        variant: 'styles.button',
        bg: theme === 'light' ? 'rgba(248, 250, 252, 0.8)' : 'rgba(17, 24, 39, 0.8)', // Soft backgrounds
        borderRadius: 'circle',
        p: 2,
        cursor: 'pointer',
        border: 'none',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: '44px',
        height: '44px',
        backdropFilter: 'blur(10px)',
        transition: 'all 0.5s cubic-bezier(0.25, 0.1, 0.25, 1)', // Smooth easing
        position: 'relative',
        overflow: 'visible',
        boxShadow: theme === 'light'
          ? '0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08)'
          : '0 4px 6px rgba(0, 0, 0, 0.3), 0 1px 3px rgba(0, 0, 0, 0.2)',
        '&:before': {
          content: '""',
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          borderRadius: '50%',
          background: theme === 'light'
            ? 'linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(147, 197, 253, 0.1))'
            : 'linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(124, 58, 237, 0.2))',
          opacity: 0,
          transition: 'opacity 0.3s ease'
        },
        '&:hover': {
          transform: 'translateY(-2px) scale(1.05)',
          boxShadow: theme === 'light'
            ? '0 10px 25px rgba(0, 0, 0, 0.15), 0 4px 6px rgba(0, 0, 0, 0.1)'
            : '0 10px 25px rgba(0, 0, 0, 0.4), 0 4px 6px rgba(0, 0, 0, 0.3)',
          '&:before': {
            opacity: 1
          }
        },
        '&:focus': {
          outline: '2px solid',
          outlineColor: theme === 'light' ? 'blue.500' : 'indigo.500',
          outlineOffset: '2px'
        }
      }}
    >
      <span
        role="img"
        aria-label={theme === 'light' ? "sun" : "moon"}
        sx={{
          fontSize: '1.2rem',
          display: 'inline-block',
          transition: 'transform 0.6s ease-in-out, opacity 0.3s ease',
          transform: `rotate(${theme === 'light' ? 0 : 180}deg)`,
          transformOrigin: 'center',
          position: 'relative',
          zIndex: 2
        }}
      >
        {theme === 'light' ? '☀️' : '🌙'}
      </span>
    </button>
  );
};

export default ThemeToggle;