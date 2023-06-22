import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8000/api/';

axios.interceptors.response.use(
    resp => resp, async error => {
        if (error.response.status === 401) {
            console.log("401");
            const response = await axios.post("refresh", {}, { withCredentials: true });
            if (response.status === 200) {
                console.log("200");
                console.log(response.data.token);
                const AUTH_TOKEN = `Bearer ${response.data.token}`
                localStorage.setItem('token', AUTH_TOKEN);
                axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
                return axios.request(error.config);
            }
        }
        else {
            return error;
        }
    });