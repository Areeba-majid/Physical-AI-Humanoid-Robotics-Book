// @ts-check
// `@type` JSDoc annotations allow IDEs and type-checking tools to autocomplete
// and validate function arguments and return types for the Docusaurus `config` object.

const lightCodeTheme = require('prism-react-renderer').themes.github;
const darkCodeTheme = require('prism-react-renderer').themes.dracula;

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AI-native Physical AI & Humanoid Robotics Textbook',
  tagline: 'An interactive educational platform with AI-powered features',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://Areeba-majid.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/Physical-AI-Humanoid-Robotics-Book/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Areeba-majid', // Usually your GitHub org/user name.
  projectName: 'Physical-AI-Humanoid-Robotics-Book', // Usually your repo name.

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'ur'],
    localeConfigs: {
      ur: {
        label: 'اردو',
        direction: 'rtl',
      },
    },
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/Areeba-majid/Physical-AI-Humanoid-Robotics-Book/edit/master/',
          showLastUpdateTime: true,
          showLastUpdateAuthor: true,
        },
        blog: false, // Disable blog if not needed
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'AI Textbook Platform',
        logo: {
          alt: 'Textbook Platform Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Textbook',
          },
          { to: '/dashboard', label: 'Dashboard', position: 'left' },
          { to: '/quiz', label: 'Quizzes', position: 'left' },
          {
            type: 'localeDropdown',
            position: 'right',
            dropdownItemsAfter: [
              {
                to: '/help-translation',
                label: 'Help Translate',
              },
            ],
          },
          {
            href: 'https://github.com/Areeba-majid/Physical-AI-Humanoid-Robotics-Book',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Tutorial',
                to: '/docs/intro',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Stack Overflow',
                href: 'https://stackoverflow.com/questions/tagged/docusaurus',
              },
              {
                label: 'Discord',
                href: 'https://discordapp.com/invite/docusaurus',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/docusaurus',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/Areeba-majid/Physical-AI-Humanoid-Robotics-Book',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} AI Textbook Platform. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),

  plugins: [
    // Add custom plugins here
  ],
};

module.exports = config;