import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'A Complete, Spec-Driven Guide to Building Intelligent Humanoid Robots',
  favicon: 'img/favicon.ico',

  url: 'https://azra-humanoid-robotics.vercel.app',
  baseUrl: '/',

  organizationName: 'azra talib',
  projectName: 'humanoid-robotics-book',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.js',
          // ❌ editUrl removed — Edit this page button will disappear
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      },
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',

    navbar: {
      title: 'Humanoid Robotics Book',
      logo: {
        alt: 'Humanoid Robotics Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          to: '/',
          label: 'Home',
          position: 'left',
        },
        {
          type: 'docSidebar',
          sidebarId: 'mainSidebar',
          label: 'Book',
          position: 'left',
        },
        {
          href: 'https://github.com/Azratalib123/azra-humanoid-robotics',
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
              label: 'Book',
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'X',
              href: 'https://x.com/AzraTalib',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/Azratalib123/azra-humanoid-robotics',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Azra Talib.`,
    },

    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  },
};

export default config;

// import {themes as prismThemes} from 'prism-react-renderer';

// // .env file load karne ke liye
// require('dotenv').config();

// /** @type {import('@docusaurus/types').Config} */
// const config = {
//   title: 'Physical AI & Humanoid Robotics',
//   tagline: 'A Complete, Spec-Driven Guide to Building Intelligent Humanoid Robots',
//   favicon: 'img/favicon.ico',

//   url: 'https://azra-humanoid-robotics.vercel.app',
//   baseUrl: '/',

//   organizationName: 'azra talib',
//   projectName: 'humanoid-robotics-book',

//   onBrokenLinks: 'throw',

//   // Chatbot configuration
//   customFields: {
//     geminiApiKey: process.env.VITE_GEMINI_API_KEY,
//   },

//   i18n: {
//     defaultLocale: 'en',
//     locales: ['en'],
//   },

//   presets: [
//     [
//       'classic',
//       {
//         docs: {
//           sidebarPath: './sidebars.js',
//         },
//         blog: false,
//         theme: {
//           customCss: './src/css/custom.css',
//         },
//       },
//     ],
//   ],

//   themeConfig: {
//     navbar: {
//       title: 'Humanoid Robotics Book',
//       items: [
//         { to: '/', label: 'Home', position: 'left' },
//         { type: 'docSidebar', sidebarId: 'mainSidebar', label: 'Book', position: 'left' },
//         {
//           href: 'https://github.com/Azratalib123/azra-humanoid-robotics',
//           label: 'GitHub',
//           position: 'right',
//         },
//       ],
//     },
//     footer: {
//       style: 'dark',
//       copyright: `Copyright © ${new Date().getFullYear()} Azra Talib.`,
//     },
//     prism: {
//       theme: prismThemes.github,
//       darkTheme: prismThemes.dracula,
//     },
//   },
// };

// export default config;