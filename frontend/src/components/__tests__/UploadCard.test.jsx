import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import UploadCard from '../UploadCard';

describe('UploadCard', () => {
  it('renders upload area', () => {
    render(<UploadCard onUpload={vi.fn()} />);
    expect(screen.getByText(/drag & drop your image here/i)).toBeInTheDocument();
  });

  it('shows file input button', () => {
    render(<UploadCard onUpload={vi.fn()} />);
    expect(screen.getByText(/choose file/i)).toBeInTheDocument();
  });

  it('displays tips for best results', () => {
    render(<UploadCard onUpload={vi.fn()} />);
    expect(screen.getByText(/tips for best results/i)).toBeInTheDocument();
  });

  it('disables upload when loading', () => {
    render(<UploadCard onUpload={vi.fn()} loading={true} />);
    const button = screen.getByText(/choose file/i);
    expect(button).toBeDisabled();
  });
});
