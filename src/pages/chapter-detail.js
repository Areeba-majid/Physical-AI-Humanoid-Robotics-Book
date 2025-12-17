import { useEffect, useState } from 'react';
import { useLocation } from '@docusaurus/router';
import Head from '@docusaurus/Head';
import ChatBot from '../components/ChatBot';
import ThemeToggle from '../components/ThemeToggle';

// Simple markdown to HTML converter
const simpleMarkdownToHtml = (text) => {
  return text
    .replace(/^# (.*$)/gm, '<h1 class="text-3xl font-bold mt-6 mb-4">$1</h1>')
    .replace(/^## (.*$)/gm, '<h2 class="text-2xl font-semibold mt-5 mb-3">$1</h2>')
    .replace(/^### (.*$)/gm, '<h3 class="text-xl font-medium mt-4 mb-2">$1</h3>')
    .replace(/\*\*(.*?)\*\*/g, '<strong class="font-semibold">$1</strong>')
    .replace(/\*(.*?)\*/g, '<em class="italic">$1</em>')
    .replace(/\n\n/g, '</p><p class="my-4">')
    .replace(/\n/g, '<br />')
    .replace(/^(.*)$/gm, '<p class="my-4">$1</p>')
    .replace(/<p class="my-4"><\/p>/g, '')
    .replace(/<p class="my-4">(<h[1-3].*<\/h[1-3]>)<\/p>/g, '$1'); // Handle headings properly
};

const ChapterDetail = () => {
  const location = useLocation();
  const [chapter, setChapter] = useState(null);
  const [loading, setLoading] = useState(true);
  const [showChat, setShowChat] = useState(false);

  useEffect(() => {
    // Extract chapter ID from URL
    const pathSegments = location.pathname.split('/');
    const chapterId = pathSegments[pathSegments.length - 1];

    // In a real implementation, this would fetch data from the backend API
    // For now, we'll use mock data based on the ID
    const mockChapters = {
      '1': {
        id: '1',
        title: 'Introduction to AI & Robotics',
        order_index: 1,
        content: '# Introduction to AI & Robotics\n\nArtificial Intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.\n\n## What is Robotics?\n\nRobotics is an interdisciplinary branch of engineering and science that includes mechanical engineering, electrical engineering, computer science, and others. Robotics deals with the design, construction, operation, and use of robots, as well as computer systems for their control, sensory feedback, and information processing.',
        content_ur: '# مصنوعی ذہانت اور روبوٹکس کا تعارف\n\nمصنوعی ذہانت (AI) مشینوں کی طرف سے ظاہر کی جانے والی ذہانت ہے، جو انسانوں اور جانوروں کے ذہانت کے مقابل ہے۔',
        sections: [
          { title: 'What is AI?', content: 'Artificial Intelligence (AI) is intelligence demonstrated by machines...' },
          { title: 'What is Robotics?', content: 'Robotics is an interdisciplinary branch of engineering and science...' }
        ],
        word_count: 1500,
        reading_time_estimate: 7,
        associated_quiz_id: 'quiz-1',
        status: 'published',
        created_at: '2023-01-01T00:00:00Z',
        updated_at: '2023-01-02T15:30:00Z'
      },
      '2': {
        id: '2',
        title: 'Machine Learning Fundamentals',
        order_index: 2,
        content: '# Machine Learning Fundamentals\n\nMachine learning (ML) is a type of artificial intelligence that allows software applications to become more accurate at predicting outcomes without being explicitly programmed to do so. Machine learning algorithms use historical data as input to predict new output values.\n\n## Supervised Learning\n\nSupervised learning algorithms are trained using labeled examples, which means that the input data is paired with the correct output.',
        content_ur: '# مشین لرننگ کے بنیادیات\n\nمشین لرننگ (ML) مصنوعی ذہانت کی ایک قسم ہے جو سافٹ ویئر ایپلی کیشنز کو نتائج کی پیش گوئی میں زیادہ درست بنا دیتی ہے...',
        sections: [
          { title: 'What is ML?', content: 'Machine learning (ML) is a type of artificial intelligence...' },
          { title: 'Supervised Learning', content: 'Supervised learning algorithms are trained using labeled examples...' }
        ],
        word_count: 2100,
        reading_time_estimate: 10,
        associated_quiz_id: 'quiz-2',
        status: 'published',
        created_at: '2023-01-03T00:00:00Z',
        updated_at: '2023-01-04T10:15:00Z'
      }
    };

    // Simulate API call
    setTimeout(() => {
      const foundChapter = mockChapters[chapterId];
      setChapter(foundChapter);
      setLoading(false);
    }, 500);
  }, [location.pathname]);

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="text-center py-20">
          <p className="text-lg">Loading chapter...</p>
        </div>
      </div>
    );
  }

  if (!chapter) {
    return (
      <div className="container mx-auto px-4 py-8">
        <div className="text-center py-20">
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-4">Chapter Not Found</h1>
          <p className="text-lg text-gray-600 dark:text-gray-300">The requested chapter could not be found.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <Head>
        <title>{chapter.title} | AI Textbook Platform</title>
        <meta name="description" content={`Learn about ${chapter.title} in the AI & Robotics textbook`} />
      </Head>

      <div className="flex justify-end mb-6">
        <ThemeToggle />
      </div>

      <h1 className="text-3xl md:text-4xl font-bold text-gray-900 dark:text-white mb-2">
        {chapter.order_index}. {chapter.title}
      </h1>

      <div className="flex flex-wrap gap-4 mb-6 text-sm text-gray-600 dark:text-gray-400">
        <span>{chapter.word_count} words</span>
        <span>~{chapter.reading_time_estimate} min read</span>
      </div>

      <div
        className="prose prose-lg dark:prose-invert max-w-none bg-white dark:bg-gray-800 rounded-lg shadow p-6 mb-6"
        dangerouslySetInnerHTML={{ __html: simpleMarkdownToHtml(chapter.content) }}
      />

      <div className="flex flex-wrap gap-4 mt-6">
        <button
          onClick={() => setShowChat(!showChat)}
          className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
        >
          {showChat ? 'Hide Q&A' : 'Ask Questions'}
        </button>
        {chapter.associated_quiz_id && (
          <a
            href={`/quiz/${chapter.associated_quiz_id}`}
            className="px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors"
          >
            Take Quiz
          </a>
        )}
      </div>

      {showChat && <ChatBot context={{ chapterId: chapter.id, chapterTitle: chapter.title }} />}
    </div>
  );
};

export default ChapterDetail;