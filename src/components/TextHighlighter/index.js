/** @jsxRuntime classic */
/** @jsx jsx */
import { jsx, Box } from 'theme-ui';
import React, { useState, useRef, useEffect } from 'react';

const TextHighlighter = ({ children, onTextSelection }) => {
  const [selection, setSelection] = useState(null);
  const [showMenu, setShowMenu] = useState(false);
  const [menuPosition, setMenuPosition] = useState({ x: 0, y: 0 });
  const containerRef = useRef(null);

  useEffect(() => {
    const handleSelection = () => {
      const selectedText = window.getSelection().toString().trim();
      
      if (selectedText) {
        const selectionObj = window.getSelection();
        if (selectionObj.rangeCount > 0) {
          const range = selectionObj.getRangeAt(0);
          const rect = range.getBoundingClientRect();
          
          setSelection({
            text: selectedText,
            range: range
          });
          
          setMenuPosition({
            x: rect.left + window.scrollX,
            y: rect.top + window.scrollY - 40 // Position above the selection
          });
          
          setShowMenu(true);
        }
      } else {
        setShowMenu(false);
        setSelection(null);
      }
    };

    document.addEventListener('selectionchange', handleSelection);
    return () => {
      document.removeEventListener('selectionchange', handleSelection);
    };
  }, []);

  const handleAskQuestion = () => {
    if (selection && onTextSelection) {
      onTextSelection(selection.text);
    }
    setShowMenu(false);
  };

  const handleCopy = () => {
    if (selection) {
      navigator.clipboard.writeText(selection.text);
      setShowMenu(false);
    }
  };

  return (
    <Box ref={containerRef} sx={{ position: 'relative' }}>
      {children}
      
      {showMenu && (
        <Box
          sx={{
            position: 'fixed',
            top: menuPosition.y,
            left: menuPosition.x,
            backgroundColor: 'background',
            border: '1px solid',
            borderColor: 'border',
            borderRadius: 'md',
            boxShadow: 'card',
            zIndex: 1000,
            display: 'flex',
            gap: 2,
            p: 2
          }}
        >
          <button
            onClick={handleAskQuestion}
            sx={{
              bg: 'primary',
              color: 'white',
              border: 'none',
              borderRadius: 'sm',
              p: 2,
              cursor: 'pointer',
              fontSize: 0,
              '&:hover': {
                bg: 'primaryHover'
              }
            }}
          >
            Ask AI
          </button>
          <button
            onClick={handleCopy}
            sx={{
              bg: 'muted',
              border: 'none',
              borderRadius: 'sm',
              p: 2,
              cursor: 'pointer',
              fontSize: 0,
              '&:hover': {
                bg: 'gray.3'
              }
            }}
          >
            Copy
          </button>
        </Box>
      )}
    </Box>
  );
};

export default TextHighlighter;