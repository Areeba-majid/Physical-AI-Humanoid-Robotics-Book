# TextHighlighter Component

The TextHighlighter component allows users to select text and provides a contextual menu with options to interact with the selected text.

## Usage

```jsx
import TextHighlighter from './components/TextHighlighter';

// In your content component
<TextHighlighter onTextSelection={(selectedText) => {
  // Handle the selected text (e.g., send to AI service)
  console.log('Selected text:', selectedText);
}}>
  {/* Your content here */}
  <p>This is sample content that can be highlighted.</p>
</TextHighlighter>
```

## Features

- Detects text selection by the user
- Shows a contextual menu with action buttons
- Provides "Ask AI" button to send selected text to AI service
- Provides "Copy" button to copy selected text
- Positions the menu near the selected text
- Automatically hides when user deselects text

## Implementation Details

- Uses the browser's Selection API to detect text selection
- Implements custom event handling for selection changes
- Positions the menu above the selected text
- Includes accessibility considerations