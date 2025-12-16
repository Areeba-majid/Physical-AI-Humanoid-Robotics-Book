import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '5ff'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '5ba'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'a2b'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'c3c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '156'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '88c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '000'),
    exact: true
  },
  {
    path: '/chapter-detail',
    component: ComponentCreator('/chapter-detail', '79c'),
    exact: true
  },
  {
    path: '/chapters',
    component: ComponentCreator('/chapters', '8c9'),
    exact: true
  },
  {
    path: '/dashboard',
    component: ComponentCreator('/dashboard', '857'),
    exact: true
  },
  {
    path: '/help-translation',
    component: ComponentCreator('/help-translation', '3a4'),
    exact: true
  },
  {
    path: '/quiz',
    component: ComponentCreator('/quiz', 'cdf'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', '715'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', 'cd4'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', '264'),
            routes: [
              {
                path: '/docs/ai-features/rag-chatbot',
                component: ComponentCreator('/docs/ai-features/rag-chatbot', '12d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/ai-features/translation',
                component: ComponentCreator('/docs/ai-features/translation', '317'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/chapter1',
                component: ComponentCreator('/docs/chapter1', '397'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/getting-started',
                component: ComponentCreator('/docs/getting-started', '2a1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/intro',
                component: ComponentCreator('/docs/intro', '61d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/personalization/',
                component: ComponentCreator('/docs/personalization/', '03f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/personalization/dashboard',
                component: ComponentCreator('/docs/personalization/dashboard', '32a'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/quizzes/',
                component: ComponentCreator('/docs/quizzes/', '8ea'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/quizzes/chapter1-quiz',
                component: ComponentCreator('/docs/quizzes/chapter1-quiz', '654'),
                exact: true
              },
              {
                path: '/docs/quizzes/chapter2-quiz',
                component: ComponentCreator('/docs/quizzes/chapter2-quiz', '656'),
                exact: true
              },
              {
                path: '/docs/quizzes/chapter3-quiz',
                component: ComponentCreator('/docs/quizzes/chapter3-quiz', '578'),
                exact: true
              },
              {
                path: '/docs/quizzes/chapter4-quiz',
                component: ComponentCreator('/docs/quizzes/chapter4-quiz', '51c'),
                exact: true
              },
              {
                path: '/docs/quizzes/final',
                component: ComponentCreator('/docs/quizzes/final', '502'),
                exact: true
              },
              {
                path: '/docs/quizzes/midterm',
                component: ComponentCreator('/docs/quizzes/midterm', '960'),
                exact: true
              },
              {
                path: '/docs/textbook/chapter2',
                component: ComponentCreator('/docs/textbook/chapter2', '80d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/textbook/chapter3',
                component: ComponentCreator('/docs/textbook/chapter3', 'e17'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/textbook/chapter4',
                component: ComponentCreator('/docs/textbook/chapter4', '805'),
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
    path: '/',
    component: ComponentCreator('/', '2e1'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
