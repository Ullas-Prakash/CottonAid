import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import Toast from '../Toast';

describe('Toast', () => {
  it('renders success toast', () => {
    render(<Toast type="success" message="Test message" onClose={vi.fn()} />);
    expect(screen.getByText('Test message')).toBeInTheDocument();
  });

  it('renders error toast', () => {
    render(<Toast type="error" message="Error message" onClose={vi.fn()} />);
    expect(screen.getByText('Error message')).toBeInTheDocument();
  });

  it('calls onClose when close button clicked', () => {
    const onClose = vi.fn();
    render(<Toast type="success" message="Test" onClose={onClose} />);
    
    const closeButton = screen.getByLabelText(/close notification/i);
    fireEvent.click(closeButton);
    
    expect(onClose).toHaveBeenCalled();
  });
});
