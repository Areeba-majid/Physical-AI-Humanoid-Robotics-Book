import { useEffect, useState } from 'react';
import Head from '@docusaurus/Head';
import Link from '@docusaurus/Link';
import { useLocation } from '@docusaurus/router';


const ChapterList = () => {
  const [chapters, setChapters] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // In a real implementation, this would fetch data from the backend API
    // For now, we'll use mock data
    const mockChapters = [
      {
        id: '1',
        title: 'Introduction to AI & Robotics',
        order_index: 1,
        word_count: 1500,
        reading_time_estimate: 7,
        status: 'published',
        path: '/docs/textbook/chapter1' // Docusaurus doc path
      },
      {
        id: '2',
        title: 'Machine Learning Fundamentals',
        order_index: 2,
        word_count: 2100,
        reading_time_estimate: 10,
        status: 'published',
        path: '/docs/textbook/chapter2' // Docusaurus doc path
      },
      {
        id: '3',
        title: 'Deep Learning and Neural Networks',
        order_index: 3,
        word_count: 1800,
        reading_time_estimate: 8,
        status: 'published',
        path: '/docs/textbook/chapter3' // Docusaurus doc path
      },
      {
        id: '4',
        title: 'Robotics and Automation',
        order_index: 4,
        word_count: 2200,
        reading_time_estimate: 11,
        status: 'draft',
        path: '/docs/textbook/chapter4' // Docusaurus doc path
      }
    ];

    // Simulate API call
    setTimeout(() => {
      setChapters(mockChapters);
      setLoading(false);
    }, 500);
  }, []);

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="text-center py-20">
          <p className="text-lg">Loading chapters...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <Head>
        <title>Textbook Chapters | AI Textbook Platform</title>
        <meta name="description" content="Browse all chapters of the AI & Robotics textbook" />
      </Head>

      <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-2">
        Textbook Chapters
      </h1>

      <p className="text-lg text-gray-600 dark:text-gray-300 mb-8 max-w-3xl">
        Explore all chapters in the AI & Robotics textbook. Each chapter builds on the previous one to provide a comprehensive learning experience.
      </p>

      <ul className="space-y-4">
        {chapters
          .filter(chapter => chapter.status === 'published')
          .map((chapter) => (
            <li
              key={chapter.id}
              className="bg-white dark:bg-gray-800 rounded-lg shadow-md border border-gray-200 dark:border-gray-700 p-6 transition-all hover:shadow-lg"
            >
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
                <Link
                  to={chapter.path}
                  className="text-blue-600 dark:text-blue-400 hover:underline"
                >
                  {chapter.order_index}. {chapter.title}
                </Link>
              </h3>

              <div className="flex flex-wrap gap-4 mt-3 text-sm text-gray-600 dark:text-gray-400">
                <span>{chapter.word_count} words</span>
                <span>~{chapter.reading_time_estimate} min read</span>
              </div>
            </li>
          ))
        }
      </ul>
    </div>
  );
};

export default ChapterList;