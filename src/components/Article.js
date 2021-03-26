import React, { useEffect, useState } from 'react'
import Axios from 'axios'

const Article = () => {
    const [country, setcountry] = useState([])
    useEffect(()=>{
        const lol=async()=>{
            await Axios({
                method:'',
                url:'http://127.0.0.1:8000/api/'
            })
            .then((res)=>{console.log(res.data); setcountry(res.data)})
            .catch((err)=>{console.log(err);})
        }
        lol()

    },[])
    return (

        <ul>
            {
                country.map((item,index)=>{
                    return <li key={index}>{item.title}</li>
                })
            }
        </ul>

    )
}

export default Article
