# InteractiveChapter Component

The InteractiveChapter component wraps Docusaurus content with interactive features like AI Q&A and quizzes.

## Usage

```jsx
import InteractiveChapter from './components/InteractiveChapter';

// In your Docusaurus markdown file
<InteractiveChapter 
  chapterData={{
    id: '1',
    title: 'Introduction to AI & Robotics',
    order_index: 1,
    word_count: 1500,
    reading_time_estimate: 7,
    associated_quiz_id: 'quiz-1'
  }}
>
  {/* Your chapter content goes here */}
  <h1>Introduction to AI & Robotics</h1>
  <p>Content of the chapter...</p>
</InteractiveChapter>
```

## Features

- Displays chapter metadata (title, word count, reading time)
- Includes a theme toggle for light/dark mode
- Provides an AI Q&A feature that allows users to ask questions about the content
- Links to associated quizzes
- Responsive design that works on all device sizes
- Dark mode support

## Implementation Details

- Uses Tailwind CSS for styling
- Integrates with the ChatBot component for AI Q&A
- Designed to work within Docusaurus documentation structure