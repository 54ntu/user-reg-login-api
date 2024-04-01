import React from 'react'
import {useForm} from 'react-hook-form'
import axios from 'axios'
import toast from 'react-hot-toast'

const Register = () => {

    const form = useForm({
        defaultValues:{
            username:'',
            email:'',
            password:''
        }
    })

    const submitData = async(values)=>{
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/register',values);
            if(response.status==200){
                console.log('new user added')
                toast.success('new user added successfully!!!!!!!')
            }
            
        } catch (error) {
            console.log('error submitting the data', error)
            toast.error('error on adding user data')
            
        }
    }


  return (
    <div className='main-div'>
        <h2 className='' >Registration page</h2>
        <hr></hr>
        <form onSubmit={form.handleSubmit(submitData)}>
            <label htmlFor='username'  >Username:</label>
            <input id='username' placeholder='enter your username' {...form.register('username')}/>
             <label htmlFor='email' >Email:</label>
            <input id='email' placeholder='enter your email' {...form.register('email')}/>
             <label htmlFor='password' >Password:</label>
            <input id='password' placeholder='enter your password' {...form.register('password')}/>
            <hr></hr>
            <button>submit</button>
        </form>
    </div>
  )
}

export default Register