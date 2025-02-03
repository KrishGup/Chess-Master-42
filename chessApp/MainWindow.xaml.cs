using System.Windows;
using System.Windows.Controls;

namespace chessApp
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            InitializeChessBoard();
        }

        private void InitializeChessBoard()
        {
            // Dynamically add 64 squares (buttons) to the UniformGrid 'ChessBoard'
            for (int row = 0; row < 8; row++)
            {
                for (int col = 0; col < 8; col++)
                {
                    Button square = new Button();
                    // Set alternating square colors
                    square.Background = ((row + col) % 2 == 0) ?
                        System.Windows.Media.Brushes.BurlyWood :
                        System.Windows.Media.Brushes.SaddleBrown;
                    
                    // Save position for identifying the square later
                    square.Tag = (row, col);
                    square.Click += Square_Click;
                    ChessBoard.Children.Add(square);
                }
            }
        }

        private void Square_Click(object sender, RoutedEventArgs e)
        {
            Button square = sender as Button;
            // Reset border on all squares (if needed)
            foreach (Button btn in ChessBoard.Children)
            {
                btn.BorderThickness = new Thickness(0);
            }
            // Highlight the clicked square
            square.BorderThickness = new Thickness(3);
            square.BorderBrush = System.Windows.Media.Brushes.Red;

            // Retrieve the square position from the Tag
            var (row, col) = ((int, int))square.Tag;
            outputTextBlock.Text = $"Selected square: Row {row}, Col {col}";
        }

        private void SubmitButton_Click(object sender, RoutedEventArgs e)
        {
            string inputText = inputTextBox.Text;
            outputTextBlock.Text = $"You entered: {inputText}";
        }
    }
}