import React from 'react';
//import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import LoginForm from './components/Auth.js';
import axios from 'axios';
import {HashRouter, Route,Link,Routes,BrowserRouter } from 'react-router-dom';
import Cookies from 'universal-cookie';


class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects':[],
           'token':'',
       }
   }

get_headers(){
    let headers = {
        'Content-Type': 'application/json'
    }
if (this.is_authenticated())
        {
            headers['Authorization'] = 'Token' + this.state.token
        }
        return headers
}

load_data() {
      const headers = this.get_headers()
      let one = 'http://127.0.0.1:8000/api/users/';
                 let two = 'http://127.0.0.1:8000/api/projects/';
                 const requestOne = axios.get(one, {headers} );
                 const requestTwo = axios.get(two, {headers} );
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

set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token},()=>this.load_data())
}

is_authenticated() {
        return this.state.token !== ''
}

logout() {
    this.set_token('')
}

get_token(username,password){
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username,password: password}).then(response => {
                this.set_token(response.data['token'])
                console.log(response.data)
    }
    ).catch(error => alert('Неверный логин или пароль'))
}

get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({'token': token})
}



componentDidMount() {
      this.get_token_from_storage()
      this.load_data()
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
                                <li>
                                    <Link to='/login'>Login</Link>
                                </li>
                                <li>
                               {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                               </li>
                            </ul>
                        </nav>
                            <Routes>
                                <Route exact path='/' element={ <UserList users={this.state.users} />} />
                                <Route exact path='/projects' element={ <ProjectList items={this.state.projects} />} />

                                <Route exact path='/login' element={ <LoginForm get_token={(username,
                                password) => this.get_token(username, password)} />} />

                            </Routes>
                    </BrowserRouter>

           </div>
       )
   }

}


export default App;




