import React from 'react'


const UserItem = ({user}) => {
   return (
       <tr>
           <td>
               {user.first_name}
           </td>
           <td>
               {user.username}
           </td>
           <td>
               {user.last_name}
           </td>
           <td>
                {user.uid}
           </td>
       </tr>
   )
}
const UserList = ({users}) => {
   return (
       <table>
           <th>
               First name
           </th>
           <th>
               Username
           </th>
           <th>
               Last Name
           </th>
           <th>
               UID
           </th>
           {users.map((user) => <UserItem user={user} />)}
       </table>
   )
}


export default UserList