#![cfg_attr(not(feature = "std"), no_std)]

use frame_support::{dispatch::DispatchResult, pallet_prelude::*};
use frame_system::pallet_prelude::*;
use sp_std::vec::Vec;

#[frame_support::pallet]
pub mod pallet {
    use super::*;

    #[pallet::pallet]
    #[pallet::generate_store(pub(super) trait Store)]
    pub struct Pallet<T>(_);

    #[pallet::config]
    pub trait Config: frame_system::Config {}

    #[pallet::storage]
    #[pallet::getter(fn agents)]
    pub type Agents<T: Config> = StorageMap<_, Blake2_128Concat, T::AccountId, Vec<u8>, OptionQuery>;

    #[pallet::event]
    #[pallet::generate_deposit(pub(super) fn deposit_event)]
    pub enum Event<T: Config> {
        AgentRegistered(T::AccountId, Vec<u8>),
        AgentUpdated(T::AccountId, Vec<u8>),
    }

    #[pallet::error]
    pub enum Error<T> {
        AlreadyRegistered,
        NotRegistered,
    }

    #[pallet::call]
    impl<T: Config> Pallet<T> {
        #[pallet::weight(10_000)]
        pub fn register_agent(origin: OriginFor<T>, name: Vec<u8>) -> DispatchResult {
            let who = ensure_signed(origin)?;

            ensure!(!Agents::<T>::contains_key(&who), Error::<T>::AlreadyRegistered);

            Agents::<T>::insert(&who, name.clone());
            Self::deposit_event(Event::AgentRegistered(who, name));
            Ok(())
        }

        #[pallet::weight(10_000)]
        pub fn update_agent(origin: OriginFor<T>, name: Vec<u8>) -> DispatchResult {
            let who = ensure_signed(origin)?;

            ensure!(Agents::<T>::contains_key(&who), Error::<T>::NotRegistered);

            Agents::<T>::insert(&who, name.clone());
            Self::deposit_event(Event::AgentUpdated(who, name));
            Ok(())
        }
    }
}
