import create, { SetState, GetState } from "zustand";
// import { CountSlice, createCountSlice } from "./count-slice";
import {AuthSlice, createAuthSlice} from "./auth-slice"

export type StoreState = AuthSlice;

export type StoreSlice<T> = (
  set: SetState<StoreState>,
  get: GetState<StoreState>
) => T;

const useStore = create<StoreState>((set, get) => ({
  ...createAuthSlice(set, get),
}));

export default useStore;
