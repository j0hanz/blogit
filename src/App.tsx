import '@/App.css';
import Card from '@/components/Card';

function App() {
  return (
    <div>
      <Card
        title="Sample Card"
        text="This is a sample card."
        imgSrc="https://via.placeholder.com/150"
        buttonText="Click Me"
        buttonOnClick={() => alert('Button clicked!')}
      />
    </div>
  );
}

export default App;
