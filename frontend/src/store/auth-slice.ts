import { StoreSlice } from "./store";

export interface AuthSlice {
  profileID: string;
  setProfileID: (profileID: string) => void;
}

export const initialProfileDetails = {
  id: -1,
};

// export const createAuthSlice: StoreSlice<AuthSlice> = (set, get) => ({
  export const createAuthSlice: StoreSlice<AuthSlice> = (set) => ({

  profileID: "",

  setProfileID: (profileID: string) => {
    set((prev: AuthSlice) => ({
      ...prev,
      profileID: profileID,
    }));
  },
});
