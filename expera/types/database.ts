export interface User {
    id: number;
    username: string;
    email: string;
    password: string;
    created_at: string;
  }
  
  export type NewUser = Omit<User, 'id' | 'created_at'>;