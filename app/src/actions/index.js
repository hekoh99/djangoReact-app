import axios from 'axios'
export const FETCH_CHAT = 'FETCH_CHAT';

export function fetchChat() {
  const request = axios.get('/api/chat/');
  return {
    type: FETCH_CHAT,
    payload: request
  }
}
