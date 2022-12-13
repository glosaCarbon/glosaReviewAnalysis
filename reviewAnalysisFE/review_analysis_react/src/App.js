import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Spinner from 'react-bootstrap/Spinner';
import logo from './assets/images/Glosa_logo.png'
import axios from 'axios'
import Table from 'react-bootstrap/Table';
import './App.css';

function App() {

  const [review, setReview] = useState("");
  const [response, setResponse] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    await axios.post(`http://0.0.0.0:8000/model/reviewAnalysis?ReviewInput=${review}`)
      .then((res) => setResponse(res.data), err => err);
    setLoading(false);
  }


  

  return (
    <div className="screen d-flex justify-content-center align-items-center">
      <div className='form'>

        <div className='d-flex flex-direction-column align-items-center justify-content-center'>
          <img className="logo" src={logo} />
        </div>

        <div className='d-flex flex-direction-column align-items-center justify-content-center'>
          <input value={review} className="input" type="text" placeholder="Enter your review.." onChange={(e) => setReview(e.target.value)} />
          <Button className="btn" variant="primary" onClick={() => handleSubmit()}>Submit</Button>
        </div>

        <div className='d-flex flex-direction-column align-items-center justify-content-center mt-3 mb-5'>
          {loading && <Spinner animation="border" role="status"><span className="visually-hidden">Loading...</span></Spinner>}
        </div>

        <div>
        <Table striped bordered hover variant="dark">
            <thead>
              <tr>
                <th>Review</th>
                <th>Label</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
            {!loading && response.result && response.result.map(item => 
            <tr>
              <td>{response.review}</td>
              <td>{item.label}</td>
              <td>{item.score}</td>
            </tr>)}
            </tbody>
          </Table>
        </div>
      </div>


    </div>
  );
}

export default App;
