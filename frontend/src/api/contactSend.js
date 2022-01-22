import axios from 'axios'
import { getCookie } from '../utils/getCookie'

export async function contactSend(values) {
  const response = await axios({
    method: 'post',
    url: 'http://localhost:8000/api/v1/sendmail/',
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie('csrftoken')
    },
    data: {
      author: values.author,
      title: values.title,
      body: values.body,
      category: values.category
    }
  })
  return response.data
}
