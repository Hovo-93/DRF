import React from 'react'
const ProjectItem = ({item}) => {
        return (
            <tr>
                   <td>{item.title}</td>
                   <td>{item.link}</td>
                   <td>{item.users.first_name}</td>
            </tr>
        )
}

const ProjectList = ({items}) => {
    return (
        <table>
            <tr>
                <th>Title</th>
                <th>Link</th>
                <th>Username</th>
            </tr>
            {items.map((item) => <ProjectItem item = {item}/>)}
        </table>
    )
}
export default ProjectList;