import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/Physical-AI-Humanoid-Robotics-Book/ur/chapter-detail',
    component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/chapter-detail', '521'),
    exact: true
  },
  {
    path: '/Physical-AI-Humanoid-Robotics-Book/ur/chapters',
    component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/chapters', 'a56'),
    exact: true
  },
  {
    path: '/Physical-AI-Humanoid-Robotics-Book/ur/dashboard',
    component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/dashboard', 'dba'),
    exact: true
  },
  {
    path: '/Physical-AI-Humanoid-Robotics-Book/ur/help-translation',
    component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/help-translation', '356'),
    exact: true
  },
  {
    path: '/Physical-AI-Humanoid-Robotics-Book/ur/quiz',
    component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/quiz', 'e78'),
    exact: true
  },
  {
    path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs',
    component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs', '450'),
    routes: [
      {
        path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs',
        component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs', '85f'),
        routes: [
          {
            path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs',
            component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs', '43d'),
            routes: [
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/ai-features/rag-chatbot',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/ai-features/rag-chatbot', 'cdc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/ai-features/translation',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/ai-features/translation', '4ef'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/chapter1',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/chapter1', '55d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/getting-started',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/getting-started', '4f4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/intro',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/intro', '33a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/personalization/',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/personalization/', '151'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/personalization/dashboard',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/personalization/dashboard', 'cd1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/', '694'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/chapter1-quiz',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/chapter1-quiz', '8af'),
                exact: true
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/chapter2-quiz',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/chapter2-quiz', 'e8a'),
                exact: true
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/chapter3-quiz',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/chapter3-quiz', '42e'),
                exact: true
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/chapter4-quiz',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/chapter4-quiz', '665'),
                exact: true
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/final',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/final', '0b5'),
                exact: true
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/midterm',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/quizzes/midterm', 'c71'),
                exact: true
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/textbook/chapter2',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/textbook/chapter2', 'f29'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/textbook/chapter3',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/textbook/chapter3', '95e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/Physical-AI-Humanoid-Robotics-Book/ur/docs/textbook/chapter4',
                component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/docs/textbook/chapter4', 'dbe'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/Physical-AI-Humanoid-Robotics-Book/ur/',
    component: ComponentCreator('/Physical-AI-Humanoid-Robotics-Book/ur/', '54b'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
