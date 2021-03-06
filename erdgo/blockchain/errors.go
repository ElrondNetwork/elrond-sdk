package blockchain

import "errors"

// ErrInvalidAddress signals that the provided address is invalid
var ErrInvalidAddress = errors.New("invalid address")

// ErrNilAddress signals that the provided address is nil
var ErrNilAddress = errors.New("nil address")

// ErrNilShardCoordinator signals that the provided shard coordinator is nil
var ErrNilShardCoordinator = errors.New("nil shard coordinator")
