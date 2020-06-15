import { FETCH_CHAT } from '../actions/index';

const initialState = {
    chatList: [],
};


export default function (state = initialState, action) {
    switch(action.type) {
        case FETCH_CHAT:
            return { ...state, chatList: action.payload.data };
        default:
            return state;
    }
}
