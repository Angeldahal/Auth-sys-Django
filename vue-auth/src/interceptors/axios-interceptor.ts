import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8000/api/';

let refresh = false

axios.interceptors.response.use(
    resp => resp, async error => {
        if (error.response.status === 401 && !refresh) {
            refresh = true;
            const response = await axios.post("refresh", {}, { withCredentials: true });
            if (response.status === 200) {
                const AUTH_TOKEN = `Bearer ${response.data.token}`
                localStorage.setItem('token', AUTH_TOKEN);
                error.config.headers['Authorization'] = AUTH_TOKEN;
                return await axios.request(error.config);            }
        }
        else {
            refresh = false;
            return error;
        }
    });