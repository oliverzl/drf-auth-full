import create, { SetState, GetState } from "zustand";
// import { CountSlice, createCountSlice } from "./count-slice";
import { AuthSlice, createAuthSlice } from "./auth-slice";

export type StoreState = AuthSlice;

export type StoreSlice<T> = (
  set: SetState<StoreState>,
  get: GetState<StoreState>
) => T;

const useStore = create<StoreState>((set, get) => {
  const authSlice = createAuthSlice(set, get); // Call slice to initialize it
  console.log("Initial Store State:", authSlice); // Log the initial state to verify profileID
  return {
    ...authSlice,
  };
});

export default useStore;
