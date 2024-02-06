import axios from 'axios';

export default class Api {
    public static async getHelloWorld() {
        const response = await axios.get('/hello');
        return response.data;
    }
}
