"""
User Identity Smart Contract for AlgoMingle
Manages user public keys and identity verification on Algorand
"""

from beaker import *
from pyteal import *


class UserIdentityState:
    """Global state schema for user identity contract"""
    
    # Mapping of user addresses to their public keys
    public_keys = GlobalStateMap(key_type=TealType.bytes, value_type=TealType.bytes)
    
    # Contract metadata
    total_users = GlobalStateValue(
        stack_type=TealType.uint64,
        default=Int(0),
        descr="Total number of registered users"
    )


app = Application("UserIdentity", state=UserIdentityState())


@app.external
def register_identity(public_key: abi.DynamicBytes) -> Expr:
    """Register a user's public key for secure messaging"""
    return Seq(
        # Verify the sender hasn't already registered
        Assert(app.state.public_keys[Txn.sender()].exists() == Int(0)),
        
        # Store the public key
        app.state.public_keys[Txn.sender()].set(public_key.get()),
        
        # Increment user count
        app.state.total_users.set(app.state.total_users + Int(1)),
    )


@app.external(read_only=True)
def get_public_key(user_address: abi.Address) -> abi.DynamicBytes:
    """Retrieve a user's public key"""
    return app.state.public_keys[user_address.get()]


@app.external
def update_public_key(new_public_key: abi.DynamicBytes) -> Expr:
    """Update the sender's public key"""
    return Seq(
        # Verify the sender has already registered
        Assert(app.state.public_keys[Txn.sender()].exists() == Int(1)),
        
        # Update the public key
        app.state.public_keys[Txn.sender()].set(new_public_key.get()),
    )


@app.delete(bare=True, authorize=Authorize.only(Global.creator_address()))
def delete() -> Expr:
    """Delete the application (creator only)"""
    return Approve()


if __name__ == "__main__":
    app.build().export("./artifacts/")
