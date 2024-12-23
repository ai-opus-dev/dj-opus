#![cfg_attr(not(feature = "std"), no_std)]

use frame_support::{dispatch::DispatchResult, pallet_prelude::*};
use frame_system::pallet_prelude::*;

#[frame_support::pallet]
pub mod pallet {
    use super::*;

    #[pallet::pallet]
    #[pallet::generate_store(pub(super) trait Store)]
    pub struct Pallet<T>(_);

    #[pallet::config]
    pub trait Config: frame_system::Config {}

    #[pallet::storage]
    #[pallet::getter(fn governance_account)]
    pub type GovernanceAccount<T: Config> = StorageValue<_, T::AccountId, ValueQuery>;

    #[pallet::event]
    #[pallet::generate_deposit(pub(super) fn deposit_event)]
    pub enum Event<T: Config> {
        GovernanceChanged(T::AccountId),
    }

    #[pallet::call]
    impl<T: Config> Pallet<T> {
        #[pallet::weight(10_000)]
        pub fn set_governance(origin: OriginFor<T>, new_account: T::AccountId) -> DispatchResult {
            let who = ensure_signed(origin)?;

            GovernanceAccount::<T>::put(&new_account);

            Self::deposit_event(Event::GovernanceChanged(new_account));
            Ok(())
        }
    }
}
