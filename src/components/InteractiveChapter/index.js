import { useState } from 'react';
import Head from '@docusaurus/Head';
import Link from '@docusaurus/Link';
import ChatBot from '../ChatBot';
import ThemeToggle from '../ThemeToggle';

const InteractiveChapter = ({ children, chapterData, allChapters }) => {
  const [showChat, setShowChat] = useState(false);

  if (!chapterData) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 flex items-center justify-center px-4 py-12">
        <div className="text-center max-w-2xl">
          <h1 className="font-serif text-4xl font-bold text-gray-900 dark:text-white mb-6 tracking-tight">
            Chapter Not Found
          </h1>
          <p className="text-lg text-gray-600 dark:text-gray-300 mb-8 leading-relaxed">
            The requested chapter could not be found. Please check the URL or navigate back to the textbook homepage.
          </p>
          <Link
            to="/docs/textbook"
            className="inline-block px-6 py-3 bg-gradient-to-r from-blue-500 to-teal-500 text-white font-medium rounded-lg shadow-lg hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300"
          >
            Browse Textbook
          </Link>
        </div>
      </div>
    );
  }

  // Find next and previous chapters based on order_index
  let nextChapter = null;
  let prevChapter = null;

  if (allChapters && allChapters.length > 0) {
    const currentIndex = allChapters.findIndex(ch => ch.id === chapterData.id);
    if (currentIndex !== -1) {
      if (currentIndex < allChapters.length - 1) {
        nextChapter = allChapters[currentIndex + 1];
      }
      if (currentIndex > 0) {
        prevChapter = allChapters[currentIndex - 1];
      }
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 transition-all duration-500 ease-in-out p-4 md:p-6 pb-20">
      <div className="max-w-4xl mx-auto">
        <Head>
          <title>{chapterData.title} | AI Textbook Platform</title>
          <meta name="description" content={`Learn about ${chapterData.title} in the AI & Robotics textbook`} />
        </Head>

        <div className="sticky top-4 z-10 bg-white/80 dark:bg-gray-800/80 backdrop-blur-lg rounded-xl p-4 mb-6 shadow-lg border border-gray-200/30 dark:border-gray-700/30 transition-all duration-300">
          <div className="flex flex-col md:flex-row md:justify-between md:items-start gap-4">
            <div className="flex-1">
              <h1 className="font-serif text-2xl md:text-3xl font-bold text-gray-900 dark:text-white mb-2 tracking-tight">
                {chapterData.order_index}. {chapterData.title}
              </h1>
              <div className="flex flex-wrap gap-4 mt-2 text-sm text-gray-600 dark:text-gray-400">
                <span className="flex items-center">
                  <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
                  </svg>
                  {chapterData.word_count} words
                </span>
                <span className="flex items-center">
                  <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                  ~{chapterData.reading_time_estimate} min read
                </span>
              </div>
            </div>
            <div className="flex-shrink-0">
              <ThemeToggle />
            </div>
          </div>
        </div>

        <div className="transition-all duration-500 ease-in-out bg-white dark:bg-gray-800/90 backdrop-blur-sm rounded-2xl shadow-xl border border-gray-200/30 dark:border-gray-700/30 overflow-hidden mb-8 animate-fadeIn">
          <div className="p-6 md:p-8 prose prose-lg dark:prose-invert max-w-none prose-headings:font-serif prose-headings:font-bold prose-headings:tracking-tight prose-p:leading-relaxed prose-img:rounded-lg prose-img:shadow-md">
            {children}
          </div>
        </div>

        <div className="flex flex-wrap gap-4 mb-8 justify-center">
          <button
            onClick={() => setShowChat(!showChat)}
            className="px-6 py-3 bg-gradient-to-r from-blue-500 to-indigo-600 text-white font-medium rounded-lg shadow-lg hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 dark:focus:ring-offset-gray-900"
          >
            {showChat ? (
              <span className="flex items-center">
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
                Hide Q&A
              </span>
            ) : (
              <span className="flex items-center">
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path>
                </svg>
                Ask Questions
              </span>
            )}
          </button>
          {chapterData.associated_quiz_id && (
            <Link
              to={`/quiz/${chapterData.associated_quiz_id}`}
              className="px-6 py-3 bg-gradient-to-r from-green-500 to-teal-600 text-white font-medium rounded-lg shadow-lg hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300 inline-flex items-center"
            >
              <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
              Take Quiz
            </Link>
          )}
        </div>

        {/* Chapter Navigation */}
        {(prevChapter || nextChapter) && (
          <div className="mt-12 pt-6 border-t border-gray-200 dark:border-gray-700">
            <div className="flex flex-col sm:flex-row items-center justify-between gap-6">
              <div>
                {prevChapter && (
                  <Link
                    to={prevChapter.path || `/docs/textbook/chapter${prevChapter.order_index}`}
                    className="group inline-flex items-center px-5 py-3 bg-gradient-to-r from-gray-100 to-gray-200 dark:from-gray-700 dark:to-gray-800 text-gray-800 dark:text-gray-200 font-medium rounded-lg shadow-md hover:shadow-lg transform hover:-translate-y-1 transition-all duration-300 border border-gray-300 dark:border-gray-600"
                  >
                    <svg className="w-5 h-5 mr-2 group-hover:-translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 19l-7-7 7-7"></path>
                    </svg>
                    Previous
                    <div className="ml-2 font-bold group-hover:translate-x-1 transition-transform duration-300 truncate max-w-xs">
                      {prevChapter.title}
                    </div>
                  </Link>
                )}
              </div>
              <div className="text-base text-gray-600 dark:text-gray-400 font-medium">
                Chapter <span className="font-bold text-indigo-600 dark:text-indigo-400">{chapterData.order_index}</span> of <span className="font-bold">{allChapters ? allChapters.length : '?'}</span>
              </div>
              <div>
                {nextChapter && (
                  <Link
                    to={nextChapter.path || `/docs/textbook/chapter${nextChapter.order_index}`}
                    className="group inline-flex items-center px-5 py-3 bg-gradient-to-r from-blue-500 to-indigo-600 text-white font-medium rounded-lg shadow-md hover:shadow-lg transform hover:-translate-y-1 transition-all duration-300"
                  >
                    <div className="mr-2 font-bold group-hover:-translate-x-1 transition-transform duration-300 truncate max-w-xs">
                      {nextChapter.title}
                    </div>
                    Next
                    <svg className="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7"></path>
                    </svg>
                  </Link>
                )}
              </div>
            </div>
          </div>
        )}

        {showChat && <ChatBot context={{ chapterId: chapterData.id, chapterTitle: chapterData.title }} />}
      </div>

      <style jsx>{`
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(10px); }
          to { opacity: 1; transform: translateY(0); }
        }
        .animate-fadeIn {
          animation: fadeIn 0.5s ease-out forwards;
        }
      `}</style>
    </div>
  );
};

export default InteractiveChapter;