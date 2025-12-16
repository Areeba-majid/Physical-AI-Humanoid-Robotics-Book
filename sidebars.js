// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    'intro',
    'getting-started',
    {
      type: 'category',
      label: 'Textbook Content',
      items: [
        'chapter1',
        'textbook/chapter2',
        'textbook/chapter3',
        'textbook/chapter4',
      ],
    },
    {
      type: 'category',
      label: 'AI Features',
      items: [
        'ai-features/rag-chatbot',
        'ai-features/translation',
      ],
    },
    {
      type: 'category',
      label: 'Personalization',
      items: [
        'personalization/index',
        'personalization/dashboard',
      ],
    },
    {
      type: 'category',
      label: 'Quizzes',
      items: [
        'quizzes/index',
      ],
    },
  ],
};

module.exports = sidebars;