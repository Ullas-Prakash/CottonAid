import { Leaf, Brain, Target, Users, Github, Mail } from 'lucide-react';

/**
 * About page - Information about the project
 */
const About = () => {
  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Hero */}
        <div className="text-center mb-12">
          <div className="inline-flex items-center justify-center w-20 h-20 bg-primary-100 rounded-full mb-4">
            <Leaf className="w-10 h-10 text-primary-600" />
          </div>
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            About CottonAid
          </h1>
          <p className="text-xl text-gray-600">
            AI-powered cotton disease detection for modern agriculture
          </p>
        </div>

        {/* Mission */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Our Mission</h2>
          <p className="text-gray-600 leading-relaxed mb-4">
            CottonAid is dedicated to helping farmers and agricultural professionals quickly
            and accurately identify diseases in cotton plants using cutting-edge artificial
            intelligence technology. Our goal is to enable early detection and treatment,
            reducing crop losses and improving agricultural productivity.
          </p>
          <p className="text-gray-600 leading-relaxed">
            By leveraging deep learning and computer vision, we make expert-level disease
            diagnosis accessible to everyone, anywhere, at any time.
          </p>
        </div>

        {/* Features */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <div className="card">
            <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mb-4">
              <Brain className="w-6 h-6 text-primary-600" />
            </div>
            <h3 className="text-lg font-bold text-gray-800 mb-2">
              Advanced AI Model
            </h3>
            <p className="text-gray-600 text-sm">
              Powered by DenseNet121 architecture, trained on thousands of cotton disease
              images with 97% accuracy on test data.
            </p>
          </div>

          <div className="card">
            <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mb-4">
              <Target className="w-6 h-6 text-green-600" />
            </div>
            <h3 className="text-lg font-bold text-gray-800 mb-2">
              High Accuracy
            </h3>
            <p className="text-gray-600 text-sm">
              Our model achieves high precision in detecting 6 different cotton diseases
              and healthy plants with detailed confidence scores.
            </p>
          </div>

          <div className="card">
            <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mb-4">
              <Leaf className="w-6 h-6 text-blue-600" />
            </div>
            <h3 className="text-lg font-bold text-gray-800 mb-2">
              Easy to Use
            </h3>
            <p className="text-gray-600 text-sm">
              Simply upload an image of a cotton leaf and get instant results with
              actionable recommendations for treatment.
            </p>
          </div>

          <div className="card">
            <div className="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center mb-4">
              <Users className="w-6 h-6 text-purple-600" />
            </div>
            <h3 className="text-lg font-bold text-gray-800 mb-2">
              For Everyone
            </h3>
            <p className="text-gray-600 text-sm">
              Designed for farmers, agronomists, researchers, and anyone involved in
              cotton cultivation and crop management.
            </p>
          </div>
        </div>

        {/* Technology */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Technology Stack</h2>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
            {[
              { name: 'TensorFlow', desc: 'Deep Learning' },
              { name: 'DenseNet121', desc: 'CNN Architecture' },
              { name: 'Flask', desc: 'Backend API' },
              { name: 'React', desc: 'Frontend UI' },
              { name: 'Tailwind CSS', desc: 'Styling' },
              { name: 'Python', desc: 'ML Pipeline' },
            ].map((tech) => (
              <div
                key={tech.name}
                className="p-4 bg-gray-50 rounded-lg border border-gray-200 text-center"
              >
                <p className="font-semibold text-gray-800">{tech.name}</p>
                <p className="text-xs text-gray-600 mt-1">{tech.desc}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Detectable Diseases */}
        <div className="card mb-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">
            Detectable Conditions
          </h2>
          <div className="space-y-3">
            {[
              {
                name: 'Aphids',
                desc: 'Small insects that feed on plant sap, causing leaf curling and stunted growth',
              },
              {
                name: 'Army Worm',
                desc: 'Caterpillars that consume leaves, causing significant defoliation',
              },
              {
                name: 'Bacterial Blight',
                desc: 'Bacterial infection causing water-soaked lesions and leaf spots',
              },
              {
                name: 'Healthy',
                desc: 'No disease detected - plant appears healthy',
              },
              {
                name: 'Powdery Mildew',
                desc: 'Fungal disease creating white powdery coating on leaves',
              },
              {
                name: 'Target Spot',
                desc: 'Fungal disease causing circular spots with concentric rings',
              },
            ].map((disease) => (
              <div
                key={disease.name}
                className="p-4 bg-gray-50 rounded-lg border border-gray-200"
              >
                <h3 className="font-semibold text-gray-800 mb-1">{disease.name}</h3>
                <p className="text-sm text-gray-600">{disease.desc}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Contact */}
        <div className="card text-center">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Get in Touch</h2>
          <p className="text-gray-600 mb-6">
            Have questions or feedback? We'd love to hear from you!
          </p>
          <div className="flex justify-center space-x-4">
            <a
              href="https://github.com"
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center space-x-2 px-4 py-2 bg-gray-800 text-white rounded-lg hover:bg-gray-700 transition-colors"
            >
              <Github className="w-5 h-5" />
              <span>GitHub</span>
            </a>
            <a
              href="mailto:contact@cottonaid.com"
              className="flex items-center space-x-2 px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors"
            >
              <Mail className="w-5 h-5" />
              <span>Email Us</span>
            </a>
          </div>
        </div>

        {/* Footer note */}
        <p className="text-center text-sm text-gray-500 mt-8">
          CottonAid is an open-source project aimed at supporting sustainable agriculture
          through technology.
        </p>
      </div>
    </div>
  );
};

export default About;
