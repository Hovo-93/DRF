import React from 'react';
//import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import axios from 'axios';
import {HashRouter, Route,Link,Routes,BrowserRouter } from 'react-router-dom';

class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects':[]
       }
   }

componentDidMount() {
             let one = 'http://127.0.0.1:8000/api/users/';
             let two = 'http://127.0.0.1:8000/api/projects/';
             const requestOne = axios.get(one);
             const requestTwo = axios.get(two);
             axios
               .all([requestOne, requestTwo])
               .then(
                 axios.spread((...responses) => {
                   const users = responses[0].data.results
                   const projects = responses[1].data.results
                    this.setState({
                                    'users': users,
                                     'projects':projects
                                      })
                   console.log(users,projects);
                 })
               )
               .catch(errors => {
                 // react on errors.
                 console.error(errors);
               });
}


   render () {
       return (
           <div className ="App">
                   <BrowserRouter>
                        <nav>
                             <ul>
                                <li>
                                    <Link to='/'>User</Link>
                                </li>
                                <li>
                                    <Link to='/projects'>Project</Link>
                                </li>
                            </ul>
                        </nav>
                            <Routes>
                                <Route exact path='/' element={ <UserList users={this.state.users} />} />
                                <Route exact path='/projects' element={ <ProjectList items={this.state.projects} />} />
                            </Routes>
                    </BrowserRouter>

           </div>
       )
   }

}


export default App;




