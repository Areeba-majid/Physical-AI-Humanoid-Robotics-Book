# ThemeToggle Component

The ThemeToggle component provides a user interface element for switching between light and dark themes in the AI textbook platform.

## Usage

```jsx
import ThemeToggle from './components/ThemeToggle';

// In your layout or header component
<ThemeToggle />
```

## Features

- Toggles between light and dark themes
- Saves user preference to localStorage
- Respects system preference by default
- Accessible with proper ARIA labels
- Smooth transitions between themes

## Implementation Details

- Uses React hooks (useState, useEffect) for state management
- Persists theme preference in localStorage
- Applies theme to the root document element
- Uses simple emoji icons for visual indication