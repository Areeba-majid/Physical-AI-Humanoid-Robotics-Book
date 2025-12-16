/** @jsxRuntime classic */
/** @jsx jsx */
import { jsx, Box, Container, Heading, Text, Button, Flex } from 'theme-ui';
import React, { useState, useRef, useEffect } from 'react';

const ChatBot = ({ context }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  // Mock initial message
  useEffect(() => {
    setMessages([
      {
        id: 1,
        text: "Hello! I'm your AI assistant for this textbook. How can I help you understand the content better?",
        sender: 'ai',
        timestamp: new Date()
      }
    ]);
  }, []);

  // Scroll to bottom of messages
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSendMessage = async () => {
    if (!inputMessage.trim()) return;

    // Add user message
    const userMessage = {
      id: Date.now(),
      text: inputMessage,
      sender: 'user',
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputMessage('');
    setIsLoading(true);

    // Simulate AI response after delay
    setTimeout(() => {
      const aiResponse = {
        id: Date.now() + 1,
        text: `I received your question: "${inputMessage}". In a real implementation, I would analyze the textbook content${context ? ` related to ${context.chapterTitle || context.topic}` : ''} and provide a detailed answer with citations.`,
        sender: 'ai',
        timestamp: new Date(),
        citations: context ? [{
          source: context.chapterTitle || 'Textbook Content',
          snippet: 'Relevant content snippet here',
          link: context.chapterId ? `/docs/textbook/chapter${context.chapterId}` : '#'
        }] : []
      };

      setMessages(prev => [...prev, aiResponse]);
      setIsLoading(false);
    }, 1000);
  };

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <Box
      sx={{
        position: 'fixed',
        bottom: '24px',
        right: '24px',
        zIndex: 1000,
        width: isOpen ? '420px' : 'auto',
        height: isOpen ? '560px' : 'auto',
        transition: 'all 0.4s cubic-bezier(0.23, 1, 0.32, 1)',
        '@media (max-width: 480px)': {
          width: isOpen ? 'calc(100vw - 32px)' : 'auto',
          right: '16px',
          left: '16px',
          bottom: '16px',
          height: isOpen ? '70vh' : 'auto'
        }
      }}
    >
      {!isOpen ? (
        <Button
          onClick={toggleChat}
          sx={{
            width: '64px',
            height: '64px',
            borderRadius: '50%',
            background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            color: 'white',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: '0 10px 25px rgba(102, 126, 234, 0.4)',
            cursor: 'pointer',
            overflow: 'hidden',
            position: 'relative',
            transition: 'all 0.3s cubic-bezier(0.25, 0.1, 0.25, 1)',
            border: 'none',
            '&:before': {
              content: '""',
              position: 'absolute',
              top: '-50%',
              left: '-50%',
              width: '200%',
              height: '200%',
              background: 'conic-gradient(from 0deg, transparent, rgba(255,255,255,0.8), transparent)',
              transform: 'rotate(0deg)',
              transition: 'transform 0.6s ease'
            },
            '&:after': {
              content: '""',
              position: 'absolute',
              top: '4px',
              left: '4px',
              right: '4px',
              bottom: '4px',
              borderRadius: '50%',
              background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
              zIndex: 1
            },
            '& > *': {
              position: 'relative',
              zIndex: 2
            },
            '&:hover': {
              transform: 'translateY(-4px) scale(1.05)',
              boxShadow: '0 20px 40px rgba(102, 126, 234, 0.6)',
              '&:before': {
                transform: 'rotate(360deg)'
              }
            },
            '&:active': {
              transform: 'translateY(-2px) scale(0.98)'
            }
          }}
        >
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="transition-all duration-300">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
          </svg>
          <Box
            sx={{
              position: 'absolute',
              top: '-4px',
              right: '-4px',
              backgroundColor: 'rgb(220, 38, 38)',
              color: 'white',
              borderRadius: '50%',
              width: '24px',
              height: '24px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '12px',
              fontWeight: 'bold',
              border: '2px solid white',
              zIndex: 3
            }}
          >
            🤖
          </Box>
        </Button>
      ) : (
        <Box
          sx={{
            backgroundColor: 'rgba(255, 255, 255, 0.95)',
            backdropFilter: 'blur(20px)',
            borderRadius: '24px',
            boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25), inset 0 0 0 1px rgba(255, 255, 255, 0.1)',
            display: 'flex',
            flexDirection: 'column',
            height: '100%',
            overflow: 'hidden',
            transition: 'all 0.4s cubic-bezier(0.23, 1, 0.32, 1)',
            border: '1px solid rgba(255, 255, 255, 0.2)',
            animation: 'slideUp 0.4s ease-out'
          }}
        >
          {/* Chat Header */}
          <Flex
            sx={{
              background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
              color: 'white',
              p: 4,
              justifyContent: 'space-between',
              alignItems: 'center',
              borderTopLeftRadius: '24px',
              borderTopRightRadius: '24px',
              position: 'relative',
              overflow: 'hidden',
              '&:before': {
                content: '""',
                position: 'absolute',
                top: 0,
                left: 0,
                right: 0,
                bottom: 0,
                background: 'radial-gradient(circle at top right, rgba(255,255,255,0.2) 0%, transparent 50%)'
              }
            }}
          >
            <Box sx={{ position: 'relative', zIndex: 1 }}>
              <Heading as="h3" sx={{ fontSize: 2, m: 0, fontWeight: '700' }}>
                AI Textbook Assistant
              </Heading>
              <Text as="p" sx={{ fontSize: 0, opacity: 0.9, mt: 1 }}>
                {context ? `Studying: ${context.chapterTitle || context.topic}` : 'Ask me anything about the textbook'}
              </Text>
            </Box>
            <Button
              onClick={toggleChat}
              sx={{
                backgroundColor: 'rgba(255, 255, 255, 0.2)',
                color: 'white',
                border: 'none',
                fontSize: 2,
                p: '8px',
                borderRadius: '50%',
                width: '36px',
                height: '36px',
                cursor: 'pointer',
                transition: 'all 0.2s ease',
                position: 'relative',
                zIndex: 1,
                '&:hover': {
                  backgroundColor: 'rgba(255, 255, 255, 0.3)',
                  transform: 'scale(1.1)'
                },
                '&:active': {
                  transform: 'scale(0.95)'
                }
              }}
            >
              ×
            </Button>
          </Flex>

          {/* Messages Container */}
          <Box
            sx={{
              flex: 1,
              p: 4,
              overflowY: 'auto',
              backgroundColor: 'rgba(249, 250, 251, 0.8)',
              display: 'flex',
              flexDirection: 'column',
              borderBottomLeftRadius: '16px',
              borderBottomRightRadius: '16px',
              backdropFilter: 'blur(10px)'
            }}
          >
            {messages.map((message) => (
              <Flex
                key={message.id}
                sx={{
                  mb: 4,
                  alignItems: message.sender === 'user' ? 'flex-end' : 'flex-start',
                  alignSelf: message.sender === 'user' ? 'flex-end' : 'flex-start',
                  flexDirection: message.sender === 'user' ? 'row-reverse' : 'row',
                  animation: 'fadeInUp 0.4s ease-out'
                }}
              >
                <Box
                  sx={{
                    maxWidth: '85%',
                    p: 3,
                    borderRadius: '20px',
                    backgroundColor: message.sender === 'user'
                      ? 'rgba(102, 126, 234, 0.1)'
                      : 'rgba(255, 255, 255, 0.9)',
                    color: message.sender === 'user' ? 'inherit' : 'gray.8',
                    wordWrap: 'break-word',
                    boxShadow: message.sender === 'user'
                      ? '0 4px 12px rgba(102, 126, 234, 0.15)'
                      : '0 2px 8px rgba(0, 0, 0, 0.08)',
                    border: message.sender === 'user'
                      ? '1px solid rgba(102, 126, 234, 0.2)'
                      : '1px solid rgba(0, 0, 0, 0.05)',
                    backdropFilter: 'blur(10px)',
                    position: 'relative',
                    transition: 'transform 0.2s ease',
                    '&:hover': {
                      transform: 'translateY(-2px)',
                      boxShadow: message.sender === 'user'
                        ? '0 6px 16px rgba(102, 126, 234, 0.2)'
                        : '0 4px 12px rgba(0, 0, 0, 0.1)'
                    }
                  }}
                >
                  <Text sx={{
                    fontSize: 1,
                    lineHeight: '1.6',
                    color: message.sender === 'user' ? 'rgb(55, 65, 81)' : 'inherit'
                  }}>
                    {message.text}
                  </Text>

                  {/* Citations for AI messages */}
                  {message.sender === 'ai' && message.citations && message.citations.length > 0 && (
                    <Box sx={{
                      mt: 3,
                      pt: 3,
                      borderTop: '1px solid',
                      borderColor: 'rgba(0, 0, 0, 0.1)',
                      fontSize: 0,
                      bg: 'rgba(243, 244, 246, 0.6)',
                      p: 2,
                      borderRadius: '8px',
                      backdropFilter: 'blur(5px)'
                    }}>
                      <Text sx={{ fontWeight: 'bold', mb: 2, color: 'rgb(55, 65, 81)' }}>📚 Sources:</Text>
                      {message.citations.map((citation, index) => (
                        <Box key={index} sx={{ mb: 2 }}>
                          <Text as="span" sx={{
                            fontStyle: 'normal',
                            fontWeight: '600',
                            color: 'rgb(37, 99, 235)',
                            display: 'block',
                            mb: 1
                          }}>
                            {citation.source}
                          </Text>
                          <Text as="div" sx={{
                            fontSize: '0.75rem',
                            color: 'rgb(107, 114, 128)',
                            mb: 1
                          }}>
                            "{citation.snippet}"
                          </Text>
                          {citation.link && (
                            <a
                              href={citation.link}
                              sx={{
                                fontSize: '0.75rem',
                                color: 'rgb(37, 99, 235)',
                                textDecoration: 'none',
                                fontWeight: '500',
                                '&:hover': {
                                  textDecoration: 'underline'
                                }
                              }}
                            >
                              🔗 Read more →
                            </a>
                          )}
                        </Box>
                      ))}
                    </Box>
                  )}
                </Box>
              </Flex>
            ))}

            {isLoading && (
              <Flex sx={{ mb: 4, alignItems: 'flex-start', animation: 'fadeInUp 0.4s ease-out' }}>
                <Box
                  sx={{
                    maxWidth: '85%',
                    p: 3,
                    borderRadius: '20px',
                    backgroundColor: 'rgba(255, 255, 255, 0.9)',
                    color: 'gray.600',
                    fontStyle: 'italic',
                    boxShadow: '0 2px 8px rgba(0, 0, 0, 0.08)',
                    border: '1px solid rgba(0, 0, 0, 0.05)',
                    backdropFilter: 'blur(10px)'
                  }}
                >
                  <Box sx={{ display: 'flex', alignItems: 'center' }}>
                    <Box sx={{ mr: 2 }}>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" className="animate-spin">
                        <path d="M21 12a9 9 0 1 1-6.219-8.56"></path>
                      </svg>
                    </Box>
                    <span>Analyzing textbook content...</span>
                  </Box>
                </Box>
              </Flex>
            )}
            <div ref={messagesEndRef} />
          </Box>

          {/* Input Area */}
          <Flex
            sx={{
              p: 4,
              borderTop: '1px solid',
              borderColor: 'rgba(0, 0, 0, 0.05)',
              backgroundColor: 'rgba(249, 250, 251, 0.8)',
              backdropFilter: 'blur(10px)',
              alignItems: 'center'
            }}
          >
            <Box
              sx={{
                flex: 1,
                position: 'relative',
                mr: 3
              }}
            >
              <textarea
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="Ask a question about this content..."
                disabled={isLoading}
                rows={1}
                sx={{
                  width: '100%',
                  p: '14px 20px',
                  borderRadius: '24px',
                  border: '1px solid',
                  borderColor: 'rgba(0, 0, 0, 0.1)',
                  backgroundColor: 'rgba(255, 255, 255, 0.9)',
                  backdropFilter: 'blur(10px)',
                  fontSize: 1,
                  resize: 'none',
                  minHeight: '48px',
                  maxHeight: '100px',
                  boxShadow: 'inset 0 2px 4px rgba(0, 0, 0, 0.05)',
                  transition: 'all 0.2s ease',
                  '&:focus': {
                    outline: 'none',
                    borderColor: 'rgba(102, 126, 234, 0.5)',
                    boxShadow: '0 0 0 3px rgba(102, 126, 234, 0.1), inset 0 2px 4px rgba(0, 0, 0, 0.05)'
                  },
                  '&:disabled': {
                    opacity: 0.5,
                    cursor: 'not-allowed'
                  }
                }}
              />
            </Box>
            <Button
              onClick={handleSendMessage}
              disabled={!inputMessage.trim() || isLoading}
              sx={{
                backgroundColor: inputMessage.trim() && !isLoading
                  ? 'rgba(102, 126, 234, 0.1)'
                  : 'rgba(156, 163, 175, 0.2)',
                color: inputMessage.trim() && !isLoading
                  ? 'rgb(79, 70, 229)'
                  : 'rgb(156, 163, 175)',
                borderRadius: '50%',
                width: '48px',
                height: '48px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                border: 'none',
                cursor: inputMessage.trim() && !isLoading ? 'pointer' : 'not-allowed',
                transition: 'all 0.2s ease',
                minWidth: 'auto',
                backdropFilter: 'blur(5px)',
                boxShadow: inputMessage.trim() && !isLoading
                  ? '0 4px 12px rgba(102, 126, 234, 0.15)'
                  : 'none',
                '&:hover': {
                  backgroundColor: inputMessage.trim() && !isLoading
                    ? 'rgba(102, 126, 234, 0.2)'
                    : 'rgba(156, 163, 175, 0.2)',
                  transform: inputMessage.trim() && !isLoading ? 'scale(1.05)' : 'none',
                  boxShadow: inputMessage.trim() && !isLoading
                    ? '0 6px 16px rgba(102, 126, 234, 0.25)'
                    : 'none'
                },
                '&:active': {
                  transform: inputMessage.trim() && !isLoading ? 'scale(0.95)' : 'none'
                }
              }}
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"></path>
              </svg>
            </Button>
          </Flex>

          <style jsx>{`
            @keyframes slideUp {
              from {
                opacity: 0;
                transform: translateY(100%) scale(0.8);
              }
              to {
                opacity: 1;
                transform: translateY(0) scale(1);
              }
            }

            @keyframes fadeInUp {
              from {
                opacity: 0;
                transform: translateY(20px);
              }
              to {
                opacity: 1;
                transform: translateY(0);
              }
            }

            .animate-spin {
              animation: spin 1s linear infinite;
            }

            @keyframes spin {
              from {
                transform: rotate(0deg);
              }
              to {
                transform: rotate(360deg);
              }
            }
          `}</style>
        </Box>
      )}
    </Box>
  );
};

export default ChatBot;