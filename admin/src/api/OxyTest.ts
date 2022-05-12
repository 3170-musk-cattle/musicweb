import { ref } from 'vue';
import axios from 'axios'
const request = axios.create({ baseURL: 'http://localhost:8000/req' })
export default request

export const successApi = () => {
  return request({
    url: '/test',
    method: 'get'
  })
}

export const failApi = () => {
  return request (
    {
      url: '/fail',
      method: 'get'
    }
  )
}



