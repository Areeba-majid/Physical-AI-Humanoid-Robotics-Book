# ChatBot Component

The ChatBot component provides an AI-powered chat interface for interacting with textbook content.

## Usage

```jsx
import ChatBot from './components/ChatBot';

// In your page or layout
<ChatBot context={{
  chapterId: '1',
  chapterTitle: 'Introduction to AI & Robotics',
  // or
  // topic: 'Machine Learning'
}} />
```

## Features

- Collapsible chat interface with floating button
- Real-time messaging with AI responses
- Context-aware responses based on chapter/topic
- Citation support showing sources for AI answers
- Responsive design that works on mobile and desktop
- Typing indicators and loading states
- Smooth animations and transitions

## Implementation Details

- Uses React hooks for state management
- Implements message history and threading
- Includes mock AI response functionality (would connect to backend API in production)
- Supports citations with links to relevant content
- Follows accessibility best practices