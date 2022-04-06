package mydict

import (
	"errors"
	"fmt"
)

// Dictionary type
type Dictionary map[string]string

var (
	errNotFound   = errors.New("not found")
	errWordExists = errors.New("word exists")
	errCantUpdate = errors.New("cant update non-existing word")
	errCantDelete = errors.New("cant delete non-existing word")
)

// Search word
func (d Dictionary) Search(word string) (string, error) {
	value, exists := d[word]
	if exists {
		return value, nil
	}
	return "", errNotFound
}

// Add a word to the dictionary
func (d Dictionary) Add(word, def string) error {
	_, err := d.Search(word)
	switch err {
	case errNotFound:
		d[word] = def
	case nil:
		return errWordExists
	}
	return nil
	// if err == errNotFound {
	// 	d[word] = def
	// } else if err == nil {
	// 	return errWordExists
	// }
	// return nil
}

// Update word
func (d Dictionary) Update(word, definition string) error {
	_, err := d.Search(word)
	switch err {
	case nil:
		d[word] = definition
	case errNotFound:
		return errCantUpdate
	}
	return nil
}

func (d Dictionary) Delete(word string) error {
	_, err := d.Search(word)
	switch err {
	case nil:
		delete(d, word)
		fmt.Println("Delete Success!")
	case errNotFound:
		return errCantDelete
	}
	return nil
}
