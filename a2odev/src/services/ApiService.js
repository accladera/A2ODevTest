import { getList } from "../assets/exerciseJSON";
import { processURL } from "./Constants";


export const getListExcercises = () => {
  return getList();
};

export const postData = async (data) => {
  try {
    const response = await fetch(processURL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ data }),
    });
    if (!response.ok) {
      throw new Error('API was not ok');
    }
    const responseData = await response.json();
    return responseData;
  } catch (error) {
    throw new Error('Error sending data to server');
  }
};
