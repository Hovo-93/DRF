import React from 'react'
const ProjectItem = ({item,deleteProject}) => {
        return (
            <tr>
                   <td>{item.title}</td>
                   <td>{item.link}</td>
                   <td>{item.users.first_name}</td>
                  <td><button onClick={()=>deleteProject(item.id)}
                  type='button'>Delete</button></td>
            </tr>
        )
}

const ProjectList = ({items,deleteProject}) => {
    return (
        <table>
            <tr>
                <th>Title</th>
                <th>Link</th>
                <th>Username</th>
            </tr>
            {items.map((item) => <ProjectItem item = {item} deleteProject={deleteProject} />)}
        </table>
    )
}
export default ProjectList;